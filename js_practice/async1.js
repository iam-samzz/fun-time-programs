const getMovie = () => {
    const p1 = new Promise((resolve) => {
        setTimeout(() => {
            resolve("Inception");
        }, 2000);
    });


    return p1
};


async function showMovie() {
    
    const movieName = await getMovie()
    console.log(movieName)
}

showMovie()
console.log("hello!!")
console.log("We print first!")