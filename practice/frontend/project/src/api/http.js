import axios from "axios";

var instance = axios.create(
    {
        baseURL: "http://127.0.0.1:5000",
        timeout: 1000
    }
)

export default instance