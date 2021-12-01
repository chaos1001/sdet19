import axios from "./http";

const testcase = {
    getTestcase(params){
        return axios({
            method: "get",
            url: "/testcase",
            params: params
        })
    }
}

export default testcase