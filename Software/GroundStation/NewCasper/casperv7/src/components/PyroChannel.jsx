import React from 'react';
import './PyroChannel.css';

const PyroChannel = (Props) => {
    return(
        <div className="pyro">
            <div id="channel">Pyro Channel </div>
            <div id="number">{Props.number}</div>
            <img id="emblem" src = {require('../images/PyroChannelEmblem.png')}></img>
            <div id= "status">{Props.status}</div>
        </div>
    )
}

export default PyroChannel;