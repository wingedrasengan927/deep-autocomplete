<template>
<div class="pad-container">
  <div tabindex="1" @focus="setCaret" class="autocomplete-container">
    <span @input="sendText" @keypress="preventInput" ref="editbar" class="editable" contenteditable="true"></span>
    <span class="placeholder" contenteditable="false">{{autoComplete}}</span>    
  </div>
</div>
</template>

<script>
export default {
  name: 'Autocomplete',
  data: function() {
    return {
      autoComplete: "",
      maxChars: 75,
      connection: null
    }
  },
  mounted() {
    const url = process.env.VUE_APP_URL || "ws://localhost:8000/predict"
    this.connection = new WebSocket(url);
    this.connection.onopen = () => console.log("connection established");
    this.connection.onmessage = this.receiveText;
  },
  methods: {
    setCaret() {
      const range= document.createRange()
      const sel = window.getSelection();
      const parentNode = this.$refs.editbar;

      if (parentNode.firstChild == undefined) {
        const emptyNode = document.createTextNode("");
        parentNode.appendChild(emptyNode);
      }

      range.setStartAfter(this.$refs.editbar.firstChild);
      range.collapse(true);
      sel.removeAllRanges();
      sel.addRange(range);
    },
    preventInput(event) {
      let prevent = false;      

      // handles capital letters, numbers, and punctuations input
      if (event.key == event.key.toUpperCase()) {
        prevent = true;
      }

      // exempt spacebar input
      if (event.code == "Space") {
        prevent = false;
      }

      // handle input overflow
      const nChars = this.$refs.editbar.textContent.length;
      if (nChars >= this.maxChars) {
        prevent = true;
      }

      if (prevent == true) {
        event.preventDefault();
      }
    },
    sendText() {
      const inputText = this.$refs.editbar.textContent;
      this.connection.send(inputText);
    },
    receiveText(event) {
      this.autoComplete = event.data;
    }
  }
}
</script>

<style scoped>

.pad-container {
  padding: 0;
  width: 640px;
  border-radius: 12px;
  border: medium solid;
  border-color: #ff7575;
}

.autocomplete-container {
  font-family: "Crete Round";
  font-size: 16px;
  border-radius: 8px;
  height: 32px;
  width: 100%;
  text-align: left;
  position: relative;
  background-color: rgba(255, 117, 117, 0.10);
  caret-color: #ff7575;
}

span {
  display: block;
  min-width: 1px;
  outline: none;
}

.editable {
  position: absolute;
  left: 8px;
  top: 5px;
}

.placeholder {
  color: gray;
  position: absolute;
  left: 8px;
  top: 5px;
  z-index: -1;
}

@font-face {
  font-family: "Crete Round";
  src: local("Crete Round"),
   url(../assets/fonts/Crete_Round/CreteRound-Regular.ttf) format("truetype");
}
</style>
