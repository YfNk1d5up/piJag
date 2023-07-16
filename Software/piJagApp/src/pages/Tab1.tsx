import { IonButton, IonCard, IonCardContent, IonCardSubtitle, IonCardTitle, IonCol, IonContent, IonGrid, IonHeader, IonIcon, IonImg, IonPage, IonRow, IonTitle, IonToolbar } from '@ionic/react';
import { wifi, speedometerOutline, thermometerOutline } from 'ionicons/icons';
import { useStoreState } from 'pullstate';
import { useRef, useState, useEffect } from 'react';
import CarModel from '../components/CarModel';
import { ParamStore } from '../store';
import { getIp, getPort } from '../store/Selectors';


const Tab1 = () => {
  const pageRef = useRef();

  const ip = useStoreState(ParamStore, getIp);
  const port = useStoreState(ParamStore, getPort);
  const [rpm, setRpm] = useState(0);
  const [temp, setTemp] = useState(0);
  const [fuel, setFuel] = useState(0);
  const [contact, setContact] = useState("Contact");
  const [start, setStart] = useState("Start");
  const [sync, setSync] = useState(false);
  
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
  }, [ip, port]);*/

  const jagContact = () => {
    
    let state = '0';
    if(contact=="Contact"){
      state='1';
      setContact("Contacting...");
    }
    else{
      setContact("Turning off...");
    }
    fetch('http://'+ ip + ':' + port + "/jagcontrol", {
    method: 'POST',
    mode: 'cors',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({'relay':'1', 'state':state})
  })
  .then(response => response.json())
  .then(response => { if(response.info == "ok"){
                          setRpm(response.data.rpm);
                          setTemp(response.data.temp);
                          setFuel(response.data.fuel);
                          if(response.data.state == 255){
                            setContact("Turn off")
                          }
                          else{
                            setContact("Contact");
                            setStart("Start");
                          }
                        }
                        else{
                          console.log(response.info)
                        }
  }
  )
    }
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
    }
  return (
    <IonPage ref={ pageRef }>
      
      <IonContent fullscreen>
        
        <IonGrid>
        <IonRow className={ `animate__animated animate__faster animate__fadeIn` }>
            <IonCol size="4">
              <IonCard routerLink="/favourites">
                <IonCardContent className="ion-text-center">
                  <IonIcon icon={ speedometerOutline} color="white" />
                  <IonCardTitle>{ rpm }</IonCardTitle>
                  <IonCardSubtitle>RPM</IonCardSubtitle>
                </IonCardContent>
              </IonCard>
            </IonCol>
            <IonCol size="4">
              <IonCard routerLink="/favourites">
                <IonCardContent className="ion-text-center">
                  <IonIcon icon={ thermometerOutline } color="white" />
                  <IonCardTitle>{ temp }</IonCardTitle>
                  <IonCardSubtitle>°C</IonCardSubtitle>
                </IonCardContent>
              </IonCard>
            </IonCol>
            
            <IonCol size="4">
              <IonCard routerLink="/favourites">
                <IonCardContent className="ion-text-center">
                  <IonIcon src="/assets/fuelstation.svg" color="primary" />
                  <IonCardTitle>{ fuel }</IonCardTitle>
                  <IonCardSubtitle>%</IonCardSubtitle>
                </IonCardContent>
              </IonCard>
            </IonCol>
          </IonRow>
        
          <IonRow className={ `animate__animated animate__faster animate__fadeIn` }>
            <IonCol size="12">
              <IonCard>
                <IonCardContent>
                  <IonImg alt="DC-052-EE" src="/assets/dc-052-ee.png"/>
                  
                  <div id="car">
                  <CarModel/>
                  </div>

                  <IonButton expand="block" className="ion-margin-top" disabled={!sync || contact == "Turning off..." || contact == "Contacting..."} onClick={jagContact}>{contact}</IonButton>
                  <IonButton expand="block" className="ion-margin-top" disabled={(!sync || start=="Started" || start=="Starting...")} onClick={jagStart}>{start}</IonButton>
                </IonCardContent>
              </IonCard>
            </IonCol>
          </IonRow>
          
        </IonGrid>
      </IonContent>
    </IonPage>
    
  );
};

export default Tab1;