import { Redirect, Route } from 'react-router-dom';
import {
  IonApp,
  IonIcon,
  IonLabel,
  IonRouterOutlet,
  IonTabBar,
  IonTabButton,
  IonTabs,
  setupIonicReact
} from '@ionic/react';
import { IonReactRouter } from '@ionic/react-router';
import { ellipse, carSport, settings, powerOutline, barChartOutline} from 'ionicons/icons';
import Tab1 from './pages/Tab1';
import Tab2 from './pages/Tab2';
import Tab3 from './pages/Tab3';
import Tab4 from './pages/Tab4';

/* Core CSS required for Ionic components to work properly */
import '@ionic/react/css/core.css';

/* Basic CSS for apps built with Ionic */
import '@ionic/react/css/normalize.css';
import '@ionic/react/css/structure.css';
import '@ionic/react/css/typography.css';

/* Optional CSS utils that can be commented out */
import '@ionic/react/css/padding.css';
import '@ionic/react/css/float-elements.css';
import '@ionic/react/css/text-alignment.css';
import '@ionic/react/css/text-transformation.css';
import '@ionic/react/css/flex-utils.css';
import '@ionic/react/css/display.css';

/* Theme variables */
import './theme/variables.css';

import { useEffect, useState } from 'react';
import { createStore, get, set } from './store/IonicStorage';
import { changeIp, changePort, changePassword } from './store/ParamStore';
setupIonicReact();

const App: React.FC = () => {
  useEffect(() => {
    const setupStore = async () => {

      await createStore("piJag");
      try{
        const ip = await get("ip");
        changeIp(ip);
        console.log(ip);
        const port = await get("port");
        changePort(port);
      }
      catch{
       
        console.log("setObj");
        await set("ip", "192.168.43.51");
        await set("port", "8001");
      }
    }
    setupStore();
	}, []);
  return (
  <IonApp>
    <IonReactRouter>
      <IonTabs>
        <IonRouterOutlet>
          <Route exact path="/xtype">
            <Tab1 />
          </Route>
          <Route exact path="/power">
            <Tab2 />
          </Route>
          {/*<Route path="/charts">
            <Tab3 />
          </Route>*/}
          <Route path="/param">
            <Tab4 />
          </Route>
          <Route exact path="/">
            <Redirect to="/xtype" />
          </Route>
        </IonRouterOutlet>
        <IonTabBar slot="bottom">
          <IonTabButton tab="tab1" href="/xtype">
            <IonIcon icon={carSport} />
            <IonLabel>X-Type</IonLabel>
          </IonTabButton>
          <IonTabButton tab="tab2" href="/power">
            <IonIcon icon={powerOutline} />
            <IonLabel>Power</IonLabel>
          </IonTabButton>
          {/*
          <IonTabButton tab="tab3" href="/charts">
            <IonIcon icon={barChartOutline} />
            <IonLabel>Charts</IonLabel>
        </IonTabButton>*/}
          <IonTabButton tab="tab4" href="/param">
            <IonIcon icon={settings} />
            <IonLabel>Params</IonLabel>
          </IonTabButton>
        </IonTabBar>
      </IonTabs>
    </IonReactRouter>
  </IonApp>
);
}

export default App;
