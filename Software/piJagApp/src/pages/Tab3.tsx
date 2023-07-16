import { IonButton, IonCard, IonCardContent, IonCardSubtitle, IonCardTitle, IonCol, IonContent, IonGrid, IonHeader, IonIcon, IonImg, IonPage, IonRow, IonTitle, IonToolbar, IonItem, IonList, IonSelect, IonSelectOption, IonLabel } from '@ionic/react';
import { wifi, speedometerOutline, thermometerOutline } from 'ionicons/icons';
import { useStoreState } from 'pullstate';
import { useRef, useState, useEffect } from 'react';
import { ParamStore } from '../store';
import { getIp, getPort } from '../store/Selectors';
import Chart from '../components/Chart';
import {
  insertOBD,
  getAllOBDs,
  updateOBDById,
  deleteOBDById,
  getOBDById,
  insertTrip,
  getAllTrips,
  updateTripById} from '../api'


const Tab3 = () => {
  const pageRef = useRef();

  const ip = useStoreState(ParamStore, getIp);
  const port = useStoreState(ParamStore, getPort);
  const [rpm, setRpm] = useState(0);
  const [temp, setTemp] = useState(0);
  const [fuel, setFuel] = useState(0);
  const [contact, setContact] = useState("Contact");
  const [start, setStart] = useState("Start");
  const [sync, setSync] = useState(false);
  const [OBDSelector, setOBDSelector] = useState([{"_id":"", "name":"","pid":"","rate":0}])
  const [tripSelector, setTripSelector] = useState([{"_id":"", "name":"","start":"","end":"","obds":[]}])
  const [charts, setCharts] = useState([<IonItem><IonLabel>No charts</IonLabel></IonItem>]);
  const [selectedOBDs, setSelectedOBDs] = useState([{"_id":"", "name":"","pid":"","rate":0}]);
  const [selectedTrip, setSelectedTrip] = useState({"_id":"", "name":"","start":"","end":"","obds":[]})
  useEffect(() => {
      fetch('http://'+ ip + ':' + port + "/jagcontrol", {
        method: 'GET',
        mode: 'cors',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
      }).then(response => response.json())
      .then(response => { if(contact!= (response.state == 255 ? "Turn Off": "Contact")){
                            setContact((response.state == 255 ? "Turn Off": "Contact"))
                          }
                          setRpm(response.rpm);
                          setTemp(response.temp);
                          setFuel(response.fuel);
                          setSync(true);
                        }
            )
        .catch(function(error) {
              setSync(false);
              console.log(error.message)
            })

  }, [ip, port]);
  /*
  useEffect(() => {
    const interval = setInterval(() => {

      fetch('http://'+ ip + ':' + port + "/jagcontrol", {
        method: 'GET',
        mode: 'cors',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
      }).then(response => response.json())
      .then(response => { if(contact!= (response.state == 255 ? "Turn Off": "Contact")){
                            setContact((response.state == 255 ? "Turn Off": "Contact"))
                          }
                          setRpm(response.rpm);
                          setTemp(response.temp);
                          setFuel(response.fuel);
                          setSync(true);
                        }
            )
        .catch(function(error) {
              setSync(false);
              console.log(error.message)
            })

    }, 10000);

    return () => clearInterval(interval);
  }, [ip, port]);
*/
  const reloadOBDList = () => {
    getAllOBDs()
    .then(function (response : any) {
      console.log("data" ,response.data.data);
      setOBDSelector(response.data.data);
  })
  .catch(function (error : any) {
      console.log(error);
  })
}

  const chartsOBD = (selected: any ) => {
    setSelectedOBDs(selected);
    //filter and add to trip the ones not already selected
    let chartList : any[] = [];
     selected.forEach((el : any) => chartList.push(
      <IonItem className="charts">
        <Chart key={"chart"+el._id+selectedTrip._id} className="charts" ip={ip} port={port} id_trip={selectedTrip._id} id_obd={el._id} title={el.name} line1title="Consumption (l/100km)" line2title="Fuel tank (%)"/>
      </IonItem>)
     );
     setCharts(chartList);
    }

    const startTrip = () => {
      insertTrip({"name":"new trip","start":new Date(), "end":"", "obds": selectedOBDs.map(
        (el,index) => { 
          return {"obdId":el._id,"data":[]}
        }
        )
      });


    }

    const endTrip = () => {
      const payload = {"name":selectedTrip.name, 
      "start":selectedTrip.start,
      "end":new Date(),
      "obds":selectedTrip.obds
    }
         updateTripById(selectedTrip._id,
         payload );
    }

    const reloadTripList = () => {      
      getAllTrips()
      .then(function (response : any) {    
        //console.log(response.data.data)    
        setTripSelector(response.data.data);
    })
    .catch(function (error : any) {
        console.log(error);
    })
  }
  const chartsTrip = (selected: any ) => {
    setSelectedTrip(selected);
    let chartList : any[] = [];
     selectedOBDs.forEach((el : any) => chartList.push(
      <IonItem className="charts">
        <Chart key={"chart"+el._id+selected._id} className="charts" ip={ip} port={port} id_trip={selected._id} id_obd={el._id} title={el.name} line1title="Consumption (l/100km)" line2title="Fuel tank (%)"/>
      </IonItem>)
     );
     setCharts(chartList);
    }

/*
  const jagStart = () => {
    setStart("Starting...");
    fetch('http://'+ ip + ':' + port + "/jagcontrol", {
    method: 'POST',
    mode: 'cors',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({'relay':'2', 'state':'1'})
  })
  .then(response => response.json())
  .then(response => { if(response.info == "ok"){
                          console.log("car started")
                          setStart("Started");
                          setRpm(response.data.rpm);
                          setTemp(response.data.temp);
                          setFuel(response.data.fuel);
                        }
                        else{
                          console.log(response.info)
                        }
  }
  )
    }*/
  return (
    <IonPage ref={ pageRef }>
      
      <IonContent fullscreen>
        
        <IonGrid>
          <IonRow className={ `animate__animated animate__faster animate__fadeIn` }>
          <IonList className="selectobdlist">
                <IonItem>
                <IonSelect placeholder="Select Trip" onClick={reloadTripList} onIonChange={(selection)=>chartsTrip(selection.detail.value)}>
                  {tripSelector.map((mytrip, index) => <IonSelectOption key={mytrip._id} value={mytrip}>{mytrip.name}</IonSelectOption>)}
                </IonSelect>
                </IonItem>
            </IonList>
            <IonList className="selectobdlist">
                <IonItem>
                <IonSelect placeholder="Select OBD" multiple={true} onClick={reloadOBDList} onIonChange={(selection)=>chartsOBD(selection.detail.value)}>
                  {OBDSelector.map((myobd, index) => <IonSelectOption key={myobd._id} value={myobd}>{myobd.name}</IonSelectOption>)}
                </IonSelect>
                </IonItem>
            </IonList>
          </IonRow>
        
          <IonRow className={ `animate__animated animate__faster animate__fadeIn` }>
            <IonCol size="12">
              <IonCard>
                <IonCardContent>
                <IonButton expand="block" className="ion-margin-top" onClick={startTrip}>Start Trip</IonButton>
                <IonButton expand="block" className="ion-margin-top" disabled={selectedTrip.end != null} onClick={endTrip}>End Trip</IonButton>
                  <IonList>
                  {charts}
                  </IonList>
                 
                </IonCardContent>
              </IonCard>
            </IonCol>
          </IonRow>
          
        </IonGrid>
      </IonContent>
    </IonPage>
    
  );
};

export default Tab3;