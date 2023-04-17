import React from "react";
import './ProgressBar.css';

const ProgressBar = (props) => {
    const { bgcolor, completed,} = props;
  
    const containerStyles = {
      height: '1%',
      width: '50%',
      backgroundColor: "#2d4096",
      borderRadius: 50,
      margin: 50
    }
  
    const fillerStyles = {
      height: '100%',
      width: `${completed}%`,
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
      <div id="number">{`${completed}%`}</div>
      <div id="unit"></div>
      </div>
    );
  };
  
  export default ProgressBar;