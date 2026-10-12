const isValid = false;

const p1 = new Promise((resolve,reject)=>{

    setTimeout(()=>{
        if(isValid){
            resolve("valid credentials")
        }
        else{
            reject("Invalid credentials")
        }
    },3000)

})

p1.then((result)=>{
    console.log(result)
})
.catch((err)=>{
    console.log(err)
})

console.log("this print before...!")