import './errorPop.css'
import React from 'react'

const PopUp = ({msg})=>{   
    return (
        <div className="popup-bg">
            <div className="popup-fg card">
                <h3>ERROR</h3>
                <div className="errMsg">{msg}</div>
            </div>
        </div>
    )
}

export default PopUp