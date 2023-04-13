import React from 'react';
import './Timer.css'
const Timer = (props) => {
    return (
      <div id="title">{props.hours}:{props.minute}:{props.seconds}</div>
    )
  }

export default Timer