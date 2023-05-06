import React from 'react';
import './PyroChannel.css';

const PyroChannel = (Props) => {
    let number = Props.status;
    let status;
    let showEmblem;
    if (number == 0){
        status = "Connected";
    }
    else{
        status = "Disconnected";
        showEmblem = {visibility: 'hidden'};
    }
    return(
        <div className="pyro">
            <div id="channel">Pyro Channel </div>
            <div id="number">{Props.number}</div>
            <img id="emblem" src = {require('../images/PyroChannelEmblem.png')} style={showEmblem} alt="Lit"></img>
            <div id= "status">{status}</div>
        </div>
    )
}

export default PyroChannel;