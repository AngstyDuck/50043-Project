db.createUser(
    {
      user: "user",
      pwd: "password",
      roles: [
         { role: "dbOwner", db: "AMAZON" }
      ]
    }
,
    {
        w: "majority",
        wtimeout: 5000
    }
);
db.createCollection("AMAZONMETADATA");

