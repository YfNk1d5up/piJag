import React, {useState} from "react";
import styled from "styled-components";
import {IonDatetime, IonIcon, IonModal, IonLabel} from "@ionic/react";
import {caretDown, caretDownOutline} from "ionicons/icons";

const IonModalBox = styled(IonModal)`
      --height: '45%';
      &::part(content){
        position: absolute;
        bottom: 0;
      }
`

const DateTimePickerContainer = styled.div`
    display: flex;
    flex-direction: row;
    align-content: center;
    width: 100%;
`

const ValueContainer = styled.div`
    flex-grow: 1;
`

export const DateTimePickerComponent = (props) => {
    const [value, setValue] = useState(props.value);
    const [showDialog, setShowDialog] = useState(false);

    const onClickHandler = () => {
        setShowDialog(true);
    }
    const onIonChangeHandler = (value) => {
        setValue(value);
        setShowDialog(false);
    }

    return (
        <>
            <DateTimePickerContainer onClick={onClickHandler}>
                <IonLabel>Turn {props.onoff}: {value}</IonLabel>
                <IonIcon md={caretDown} ios={caretDownOutline}/>
            </DateTimePickerContainer>
            <IonModalBox isOpen={showDialog} onDidDismiss={() => setShowDialog(false)}>
                <IonDatetime value={value}
                             presentation="time"
                             onIonChange={e => onIonChangeHandler(e.detail.value || null)}
                             size={"cover"}
                             showDefaultButtons={true}/>
            </IonModalBox>
        </>

    )
}