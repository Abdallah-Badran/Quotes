import axios from 'axios'
import { getToken } from '../browserStorage/auth'

export const getQuote = async ()=>{
    const res = await axios.get('http://localhost:5000/quote/random', {headers: {'Authorization':getToken()}})
    return res
}