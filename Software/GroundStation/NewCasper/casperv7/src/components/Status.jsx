import React from 'react';
import './Status.css'

const Status = (Props) => {
    let number = Props.status;
    let image;
    let status;
    let color;

    if (number == 0) {
        image = ".";
        status = "Waiting";
        color = {backgroundColor: '#9499c3'};
    }
    else if (number == 1) {
        image = "✓";
        status = "Normal";
        color = {backgroundColor: '#40c110'};
        
    }
    else {
        image = "X";
        status = "Abort";
        color = {backgroundColor: '#ea1515'};
    }
    return (
        <div className = "status">
            <div id="checkmark" style={color}>{image}</div>
            <div className = "descriptions">
                <h1>{Props.name}</h1>
                <h2>{status}</h2>
            </div>
        </div>
    )
}

export default Status