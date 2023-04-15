import React from 'react';
import './Dashboard.css'
import Speedometer, {
    Background,
    Arc,
    Needle,
    Progress,
    Marks,
    Indicator,
    DangerPath
  } from 'react-speedometer';



const Dashboard = (Props) => {
    let actualValue = Props.value;
    let actualMax = Props.max;
    let valueOf1000 = actualValue/actualMax * 1000;
    return (
            <div className="dashboard" >
                <Speedometer value={valueOf1000} max={1000} fontFamily='squada-one' accentColor={Props.color} width={Props.width}>
                    <Background opacity={0}/>
                    <Arc arcWidth={1} color={Props.color}/>
                    <Progress arcWidth={5} />
                    <Marks step={400} lineColor={Props.color} fontSize={0}/>
                </Speedometer>
                <div className='title'>
                    <div id="type">{Props.type}</div>
                    <div id="value">{Props.value}</div>
                    <div id="units">{Props.units}</div>
                </div>
            </div>
    )
}

export default Dashboard