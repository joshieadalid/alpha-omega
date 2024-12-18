async function getUsers() {
  try {
    const baseUrl = "https://" + domain + ".atlassian.net";

    const config = {
      method: "get",
      url: baseUrl + "/rest/api/2/users/search",
      headers: { "Content-Type": "application/json" },
      auth: auth,
      params: { maxResults: 100 }, // Número máximo de usuarios a devolver
    };
    const response = await axios.request(config);
    console.log(response.data);
    return response.data;
  } catch (error) {
    console.log("error: ");
    console.log(error.response ? error.response.data : error.message);
  }
}

const getUsersFunc2 = async () => {
  const users = await getUsers();
  const userNames = users.map((user) => user.displayName);
  console.log("Nombres de usuarios:");
  userNames.forEach((name) => console.log(name));
};
