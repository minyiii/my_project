<script>
export default {
  name: "top-bar-new",
  methods: {
    logout() {
      let oDate = new Date();
      oDate.setDate(oDate.getDate() + -1);
      document.cookie = "username" + "=" + "admin" + ";expires=" + oDate;
      alert("登出成功");
      this.$router.push("/");
    },
  },
};
</script>

<template src="./template.html"></template>
<style src="./style.css" scoped></style>