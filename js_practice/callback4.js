f1 = ()=>{

    setTimeout(()=>{
        console.log("hello! , took 3sec");

        f2 = ()=>{
            setTimeout(()=>{
                console.log("World! , took 1sec")
            },1000)
        }

        f2()
    },3000)
}
f1()