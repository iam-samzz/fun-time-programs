/* print hello(3 sec) , world(3 sec), this is(2 sec), samararan(1sec) . Each relative to revious prints, 
and the 1st pprint relative to 0*/


function hello(world)
{
    setTimeout(()=>{
        console.log("Hello t0 : 0 - 3sec")

        world(this_is)
    },3000)
}


function world(this_is)
{
    setTimeout(()=>{
        console.log("World t1: 3 - 6sec")
        this_is(samaran)
    },3000)

}

function this_is(samaran){
    setTimeout(()=>{
        console.log("This is t2: 6 - 8 sec")
        
        samaran()
    },2000)
}

function samaran(){
    setTimeout(()=>{
        console.log("Samaran! t3: 8 - 9 sec")
    },1000)
}


hello(world)