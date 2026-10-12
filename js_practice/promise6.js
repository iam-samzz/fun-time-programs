function getUser(){
    const obj = {
        "name" : "sam",
        "age" : 19
    }

    const p1 = new Promise((resolve,reject)=>{
        resolve(obj)
    })
    
    return p1
}

let response = getUser()
response.then((result)=>{
    console.log(result)
})