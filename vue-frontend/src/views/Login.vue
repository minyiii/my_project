<template>
  <div>
    <VBar />
    <div class="login">
      <div class="box p-4">
        <h2>Login</h2>
        <form action>
          <div class="form-group" @submit="SubmitHandler">
            <label for="username">Account :</label>
            <input
              type="text"
              name="username"
              id="username"
              class="form-control"
              v-model="account"
            />
          </div>
          <div class="form-group">
            <label for="password">Password :</label>
            <input
              type="password"
              name="password"
              id="password"
              class="form-control"
              v-model="password"
            />
          </div>
          <input type="submit" value="Submit" class="btn btn-dark" />
        </form>
        <p>
          No account yet?
          <router-link :to="{ name: 'Register' }">Register Now!</router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import VBar from "@/components/Navbar-Top-After/index.vue";

export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  components: {
    VBar,
  },
  // 在生成頁面的時候透過此cookie判斷是否為登入狀態
  // username 為後端傳過來的資料
  // mounted() {
  //   let allCookies = document.cookie;
  //   if (allCookies.indexOf("username") !== -1) {
  //     this.$router.push("/convert");
  //   }
  // },
  methods: {
    SubmitHandler() {
      // let data = new URLSearchParams();
      // data.append("username", this.username);
      // data.append("password", this.password);
      let postData = {
        username: this.form.username,
        password: this.form.pwd,
      };
      this.axios
        .post("http://127.0.0.1:8000/api-token-auth/", postData)
        .then(function (response) {
          console.log(response);
          // alert(response.data.msg);
          // if (response.data.status === 0) {
          //   location.href = "/convert";
          // }
          this.$router.push("/convert");
        })
        .catch(function (error) {
          console.log(error);
        });
      // 尚須修改，因牽扯password，可能需加個token
      // this.$axios.get("http://localhost:3000/user-info").then((res) => {
      //   for (i in res.data.length) {
      //     if (
      //       this.username == res.data[i].username &&
      //       this.password == res.data[i].password
      //     ) {
      //       localStorage.setItem("token", "ImLogin");
      //       this.$router.push("/convert");
      //     } else {
      //       alert("login failed");
      //     }
      //   }
      // });
    },
  },
};
</script>

<style scoped>
.login {
  width: 100%;
  height: 92vh;
}
.box {
  margin: auto;
  background: white;
  border: 1px solid #e2dada;
  width: 50%;
  height: 400px;
  position: relative;
  top: 100px;
}
.box .btn {
  width: 100%;
  margin-top: 10px;
  margin-bottom: 15px;
  background: #fa5959;
  border: none;
  transition: 0.2s;
}
.box .btn:hover {
  background: #d01414;
}
.box p {
  text-align: center;
}
h2 {
  text-align: left;
}
.form-group {
  margin-top: 30px;
  margin-bottom: 30px;
  text-align: left;
}
@media screen and (max-width: 760px) {
  .login {
    height: 110vh;
  }
  .box {
    width: 70%;
    height: 70%;
    margin-bottom: 30px;
  }
}
@media screen and (max-height: 500px) {
  .login {
    height: 170vh;
  }
}
</style>