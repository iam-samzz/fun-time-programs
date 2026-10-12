const p1 = new Promise((resolve,reject)=>{

    
    resolve(5)
})

p1.then((result)=>{
    result *= 3
    return result
}).then((result2)=>{
    console.log(result2)
})


