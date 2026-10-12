const p1 = new Promise((resolve,reject)=>{

    setTimeout(()=>{
        resolve("")
    },3000)
})


p1
.then((result)=>{
    setTimeout(()=>{
        console.log("hello")
    },1000)
    return
})
.then(()=>{
    setTimeout(()=>{
        console.log("world")
    },3000)
})