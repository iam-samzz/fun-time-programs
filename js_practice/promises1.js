function executor(resolve, reject)
{
    return reject("not done!")
    //return reject("not done")
}

const p1 = new Promise(executor)

p1.catch((e)=>{
    console.log(e)
})
console.log(p1)