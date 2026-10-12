//helper functions
const fetchUserData = (userId) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve({ id: userId, name: "Alice", role: "Admin" });
        }, 1500);
    });
};

const fetchUserOrders = (userId) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(["Order #101", "Order #102", "Order #103"]);
        }, 1500);
    });
};

// -------------

async function loadUserAndOrders(userId){
    try{
        const usrObj = await fetchUserData(userId)
        const usrId = usrObj.id
        try{
            const usrOrder = await fetchUserOrders(usrId)
            console.log(usrObj.name)
            console.log(usrOrder)
        }
        catch(err2)
        {
            console.log(err2)
        }
    }
    catch (err)
    {
        console.log(err)
    }


}

loadUserAndOrders(1)

console.log("Loading..")
