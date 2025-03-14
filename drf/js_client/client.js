const contentContainer = document.getElementById("content-container")
const loginForm = document.getElementById("login-form")
const searchForm = document.getElementById("search-form")
const baseEndpoint = "http://localhost:8000/api"

if (loginForm) {
    // handle this login form
    loginForm.addEventListener('submit', handleLogin)
}

if (searchForm) {
    // handle this login form
    searchForm.addEventListener('submit', handleSearch)
}

function handleLogin(event) {
    event.preventDefault()
    const loginEndpoint = '${baseEndpoint}/token/'
    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData)
    let bodyStr = JSON.stringify(loginObjectData)
    console.log(loginObjectData, bodyStr  )
    // console.log(loginObjectData)
    const options = {
        method: "POST",
        headers : { 
            "Content-Type" : "application/json"
        },
        body : bodyStr
    }   


    fetch(loginEndpoint, options) // promise
    .then(response=>{
        return response.json()
    })
    .then(authData => {
        handleAuthData(authData, getProductList)
    })
    .catch(err=>{
        console.log('err', err)
    })
}

function handleAuthData(authData, callback) {
    localStorage.setItem('access', authData.access) 
    localStorage.setItem('refresh', authData.refresh)
    if (callback) {
        callback()
    }
}

function writeToContainer(data) {
    if (contentContainer) {
        contentContainer.innerHTML = "<pre>" + JSON.stringify(data) + "</pre>"
    }
}

function getFetchOptions(method, body){
     return {
        method : method === null ? "GET": method,
        headers : {
            "Content-Type": "application/json",
            "Authorization": `Bearer abc ${localStorage.getItem('access')}`
        },
        body: body ? body : null 
    } 
}

function isTokenNotValid(jsonData){
    if (jsonData.code && jsonData.code === "token_not_valid"){
        // run a refresh token fetch
        alert("Please logon again")
        return false
    }
    return true
}

function getProductList(){
    const endpoint = `${baseEndpoint}/products/`
    const options = getFetchOptions()
    fetch (endpoint, options)
    .then (response => {
        return response.json()
    })
    .then(data => {
        const validData = isTokenNotValid(data)
        if (validData) {
            writeToContainer(data)
        }
    })
}

getProductList()