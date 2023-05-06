import React from 'react';
import './Dashboard.css'
import Speedometer, {
    Background,
    Arc,
    Progress,
    Marks,
  } from 'react-speedometer';



const Dashboard = (Props) => {
    let actualValue = Props.value; //Value being currently recieved
    let actualMax = Props.range; //The range of possible numbers, not actual max but actual max can be found doing actualMin + actualMax
    let actualMin = Props.min; //The minimum value it could be
    let valueToZero = actualValue - actualMin; //Minimum should now be zero
    let valueOf1000 = valueToZero/actualMax * 1000; //Scale adjusted to fit 1000
    return (
            <div className="dashboard">
                <Speedometer value={valueOf1000} max={1000} fontFamily='squada-one' accentColor={Props.color} width={Props.width}>
                    <Background opacity={0}/>
                    <Arc arcWidth={1} color={Props.color}/>
                    <Progress arcWidth={5} />
                    <Marks step={400} lineColor={Props.color} fontSize={0}/>
                </Speedometer>
                <div className='title'>
                    <div id="type">{Props.type}</div>
                    <div id="value">{actualValue}</div>
                    <div id="units">{Props.units}</div>
                </div>
            </div>
    )
}

export default Dashboard