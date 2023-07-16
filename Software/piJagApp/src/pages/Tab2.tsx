import { IonButton, IonCard, IonCardContent, IonCardSubtitle, IonCardTitle, IonCol, IonContent, IonGrid, IonHeader, IonIcon, IonImg, IonPage, IonRow, IonTitle, IonToolbar } from '@ionic/react';
import { wifi } from 'ionicons/icons';
import { useStoreState } from 'pullstate';
import { useRef } from 'react';
import {DateTimePickerComponent} from '../components/DateTimePicker';
import { ParamStore } from '../store';
import { getIp, getPort } from '../store/Selectors';


const Tab2 = () => {
  const pageRef = useRef();
  const ip = useStoreState(ParamStore, getIp);
  const port = useStoreState(ParamStore, getPort);
  
  return (
    <IonPage ref={ pageRef }>
      <IonContent fullscreen>
        
        <IonGrid>
          
        
          <IonRow className={ `animate__animated animate__faster animate__fadeIn` }>
            <IonCol size="12">
              <IonCard>
                <IonCardContent>
                  <IonCardTitle>Automatic</IonCardTitle>
                  <DateTimePickerComponent value="07:00" onoff="on"/>
                  <DateTimePickerComponent value="20:00" onoff="off"/>
                  <IonButton expand="block" className="ion-margin-top" routerLink="/search">Save</IonButton>
                </IonCardContent>
              </IonCard>
            </IonCol>
          </IonRow>
          <IonRow className={ `animate__animated animate__faster animate__fadeIn` }>
            <IonCol size="12">
              <IonCard>
                <IonCardContent>
                  <IonCardTitle>Manual</IonCardTitle>
                  <IonButton expand="block" className="ion-margin-top" routerLink="/search">Shutdown</IonButton>
                </IonCardContent>
              </IonCard>
            </IonCol>
          </IonRow>
        </IonGrid>
      </IonContent>
    </IonPage>
    
  );
};

export default Tab2;