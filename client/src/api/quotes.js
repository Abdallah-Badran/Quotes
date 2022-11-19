import axios from 'axios'
import { getToken } from '../browserStorage/auth'

export const getQuote = async ()=>{
    const res = await axios.get('/quote/random', {headers: {'Authorization':getToken()}})
    return res
}