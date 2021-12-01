import axios from "axios"

var instance = axios.create({
    baseURL: "http://xxx/xxx",
    timeout: 1000,
})

export default instance