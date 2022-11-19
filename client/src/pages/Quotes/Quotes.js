import React, { useEffect, useState } from "react"
import { getQuote } from "../../api/quotes"
import ErrorPop from '../../components/ErrorPop/ErrorPop'
import './quotes.css'

const Quotes = ()=>{
    const [quote, setQuote] = useState({
        author: "", 
        text: ""
    })

    const [errMsg, setErrMsg] = useState('')

    const updateQuote = async ()=>{
        try {
            const res = await getQuote()
            setQuote(res.data)
        } catch (error) {
            setErrMsg(error.response.data.message)
        }
    }

    useEffect(()=>{
        updateQuote()
    }, [])

    
    if(errMsg === ''){
        return (
                        <div className="page-wrapper">
                            <div className="quote-header-wrapper">
                                <h2 className="quote-header">Your today quote is ...</h2>
                                <button onClick={updateQuote}>New Quote</button>
                            </div>
                            <div className="quote-body-new-wrapper">
                                <p className="quote-body-wrapper">
                                    {quote.quote}
                                </p>
                                <p className="quote-author">{quote.author}</p>
                            </div>
                        </div>
        )
    }else{
        return (<ErrorPop msg={errMsg}/>)
    }
}

export default Quotes