import axios from "./http"

// 存放用例页面相关接口
const testcase = {
    getTestcase(params){
        return axios({
            method: "get",
            // 会自动接在baseUrl之后
            url: "/testcase",
            params: params,
        })
    }
}

export default testcase