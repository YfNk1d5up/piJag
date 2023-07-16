import React, { useEffect, useState } from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Line } from 'react-chartjs-2';
import faker from 'faker';
import { getTripById, getOBDById, updateTripById } from '../api';


export default function Chart(props) {
  const [labels, setLabels] = useState([])
  const [values, setValues] = useState([])
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const options = {
  responsive: true,
  maintainAspectRatio: false,
  interaction: {
    mode: 'index',
    intersect: false,
  },
  stacked: false,
  plugins: {
    title: {
      display: true,
      text: props.title,
    },
  },
  scales: {
    y: {
      type: 'linear',
      display: true,
      position: 'left',
    },
    y1: {
      type: 'linear',
      display: true,
      position: 'right',
      grid: {
        drawOnChartArea: false,
      },
    },
  },
};

useEffect(()=> {
  if( props.id_trip != undefined &&  props.id_obd != undefined ) {
    const interval = setInterval(() => {
      async function fetchTripandOBD(trip_id, obd_id ) {
        const trip = await getTripById(trip_id);
        const obd = await getOBDById(obd_id);
        if(trip.data.data.obds.filter(e => e.obdId == obd.data.data._id).length!=0){
        let current_data = trip.data.data.obds.filter(e => e.obdId == obd.data.data._id)[0].data;
        current_data.push(faker.datatype.number({ min: 800, max: 1000 }));
        setLabels(current_data.map((el,index)=>index))
        setValues(current_data.map((el,index)=>Number(el)))
        const data = [...trip.data.data.obds.filter(e => e.obdId != obd.data.data._id), {"obdId": obd.data.data._id,"data": current_data}]
        const payload = {"name":trip.data.data.name, 
        "start":trip.data.data.start,
        "end":trip.data.data.end,
        "obds": data
        }
        updateTripById(trip.data.data._id,payload );
        //console.log(current_data);
        /*
        fetch('http://'+ props.ip + ':' + props.port + "/jagcharts", {
          method: 'GET',
          mode: 'cors',
          headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json'
          },
        })
        .then(response => response.json())
        .then(response => { 
                  current_data.push(response.value);
                  setLabels(current_data.map((el,index)=>index))
                  data = [...trip.obds.filter(e => e.obdId != obd._id), {"obdId": obd._id,"data": current_data}]
                  const payload = {"name":trip.name, 
                  "start":trip.start,
                  "end":trip.end,
                  "obds": data
                }
                console.log(payload)
          //updateTripById(trip._id,payload );
        }
            )
        .catch(function(error) {
              console.log(error.message)
            })

        */
        }
        else{
          if(labels.length==0){
            setLabels([0])
          setValues([0])
          }
          else{
            console.log([...labels, labels[-1]+1]);
          setLabels([...labels, labels[-1]+1])
        setValues([...values, values[-1]])
          }
        }
      }
      fetchTripandOBD(props.id_trip, props.id_obd);
    }, 10000);
    return () => clearInterval(interval);
  }
},[])

const data = {
  labels,
  datasets: [
    {
      label: props.line1title,
      data: values,
      borderColor: 'rgb(255, 99, 132)',
      backgroundColor: 'rgba(255, 99, 132, 0.5)',
      yAxisID: 'y',
    },
    /*{
      label: props.line2title,
      data: labels.map(() => faker.datatype.number({ min: 900, max: 1100 })),
      borderColor: 'rgb(53, 162, 235)',
      backgroundColor: 'rgba(53, 162, 235, 0.5)',
      yAxisID: 'y1',
    },*/
  ],
};
return <Line id={props.id} options={options} data={data} />;
}
