function print(data)
{
    console.log(data)
}

const fetchUserData = (userId) => {
    const p1 = new Promise((resolve, reject) => {
        setTimeout(() => {
            if (userId === 1) {
                resolve({ id: 1, name: "Alice", role: "Admin" });
            } else {
                reject("Error: User not found!");
            }
        }, 2000);
    });

    return p1
};

async function getData(userId){
    
    try{
        const response = await fetchUserData(userId)
        console.log(response)
    }
    catch (err) {
        print(err)
    }
}


getData(1)
getData(2)

print("hello")
print("whatsapp!")