import { IonButton, IonCard, IonCardContent, IonCardSubtitle, IonCardTitle, IonCol, IonContent, IonGrid, IonHeader, IonIcon, IonImg, IonInput, IonItem, IonLabel, IonList, IonPage, IonRow, IonTitle, IonToolbar } from '@ionic/react';
import { wifi } from 'ionicons/icons';
import { useStoreState } from 'pullstate';
import { useRef, useState } from 'react';
import { ParamStore} from '../store';
import { changeIp, changePort, changePassword } from '../store/ParamStore';
import { getIp, getPort } from '../store/Selectors';


const Tab4 = () => {
  const pageRef = useRef();
  const ip = useStoreState(ParamStore, getIp);
  const port = useStoreState(ParamStore, getPort);
  const [params, setParams] = useState({"ip":ip, "port":port})
  const saveParams = () => {
    changeIp(params.ip);
    changePort(params.port);
  }
  
  return (
    <IonPage ref={ pageRef }>
      <IonContent fullscreen>
        
        <IonGrid>
          
        
          <IonRow className={ `animate__animated animate__faster animate__fadeIn` }>
            <IonCol size="12">
              <IonCard>
                <IonCardContent>
                  <IonList>
                    <IonItem>
                      <IonLabel>IP </IonLabel>
                      <IonInput type="text" inputmode="text" placeholder={ip} value={params.ip} onIonChange={ (e) => {setParams({"ip": e.target.value, "port":params.port})}}></IonInput>
                    </IonItem>
                    <IonItem>
                    <IonLabel>PORT </IonLabel>
                    <IonInput type="text" inputmode="text" placeholder={port} value={params.port} onIonChange={ (e) => {setParams({"ip": params.ip, "port": e.target.value})}}></IonInput>
                    </IonItem>
                  </IonList>
                  <IonButton expand="block" className="ion-margin-top" onClick={saveParams}>Save</IonButton>
                </IonCardContent>
              </IonCard>
            </IonCol>
          </IonRow>
          
        </IonGrid>
      </IonContent>
    </IonPage>
    
  );
};

export default Tab4;