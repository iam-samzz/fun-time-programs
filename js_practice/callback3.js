function hello(word)
{
    setTimeout(()=>{
        console.log("Saying hello, took: 2sec")
        world()

    },2000)
    
}

function world()
{
    setTimeout(() => {
        console.log("Saying world, took 1sec")
    }, 1000);
}
hello(world)