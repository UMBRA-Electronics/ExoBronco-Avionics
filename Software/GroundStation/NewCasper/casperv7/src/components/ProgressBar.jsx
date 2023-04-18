import React from "react";
import './ProgressBar.css';

const ProgressBar = (props) => {
    const { bgcolor, completed, units, min, max} = props;

    const ratio = Math.abs(max-min);
    console.log(Math.abs(completed)/ratio);
  
    const containerStyles = {
      height: 5,
      width: '50%',
      backgroundColor: "#2d4096",
      borderRadius: 50,
      marginLeft: 50,
      marginRight: 50
    }
  
    const fillerStyles = {
      height: '100%',
      width: `${100*Math.abs(completed)/ratio}%`,
      backgroundColor: bgcolor,
      borderRadius: 'inherit',
      textAlign: 'right'
    }
  
    const labelStyles = {
      padding: 5,
      color: 'white',
      fontWeight: 'bold'
    }
  
    return (
      <div className="everything">
      <div style={containerStyles}>
        <div style={fillerStyles}>
          <span style={labelStyles}></span>
        </div>
      </div>
      <div id="number">{`${completed} ${units}`}</div>
      </div>
    );
  };
  
  export default ProgressBar;