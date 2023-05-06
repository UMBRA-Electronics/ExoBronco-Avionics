import React from "react";
import './ProgressBar.css';

const ProgressBar = (props) => {
    const { bgcolor, value, units, min, range} = props;

    let actualValue = value; //Value being currently recieved
    let actualMax = range; //The range of possible numbers, not actual max but actual max can be found doing actualMin + actualMax
    let actualMin = min; //The minimum value it could be
    let valueToZero = actualValue - actualMin; //Minimum should now be zero
    let valueOf100 = valueToZero/actualMax * 100; //Scale adjusted to fit 1000
    
  
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
      width: `${valueOf100}%`,
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
      <div id="number">{`${value} ${units}`}</div>
      </div>
    );
  };
  
  export default ProgressBar;