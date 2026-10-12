function hello(world)
{
    setTimeout(()=>{
        console.log("Saying hello! , took 2sec")
    },2000)

    world()
}


function world()
{
    setTimeout(()=>{
        console.log("Saying World! , took 1sec")
    }, 1000)

}

hello(world)


/*here hello should come 1st, and world should some second, but sdue to asyncronous system, 1sec  program executed
 first */

 