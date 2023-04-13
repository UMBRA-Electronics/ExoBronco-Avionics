import React from 'react';
import './Status.css'

const Status = (Props) => {
    return (
        <div className = "status">
            <div id="checkmark">✓</div>
            <div className = "descriptions">
                <h1>{Props.name}</h1>
                <h2>{Props.status}</h2>
            </div>
        </div>
    )
}

export default Status