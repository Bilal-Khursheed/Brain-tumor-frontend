const express = require("express");
const { spawn } = require("child_process");
const cors = require("cors");
const app = express();
app.use(cors());

const multer = require("multer");

const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, "./uploads1/");
  },
  filename: function (req, file, cb) {
    cb(null, req.query.name + file.originalname);
  },
});

const upload = multer({ storage: storage });
app.get("/hello", (req, res) => {
  var dataToSend;
  //const url = req.query.name;
  //console.log("here is the url" + url);
  // spawn new child process to call the python script C:\Users\DELL\Desktop\FYP backend algo\Brain tumor frontend\static\uploads1\00000.mnc
  //const python = spawn("python", ["strip.py", ``]);
  // collect data from script
  /* python.stdout.on("data", function (data) {
    console.log("Pipe data from python script ...");
    dataToSend = data.toString();
  });
  // in close event we are sure that stream from child process is closed
  python.on("close", (code) => {
    console.log(`child process close all stdio with code ${code}`);
    // send data to browser
    // res.send(dataToSend);*/
  return res.json({
    withoutskull: `C:/Users/DELL/Desktop/FYP backend algo/Brain tumor frontend/static/uploads1/withoutskull.gif`,
    withskull:
      "C:/Users/DELL/Desktop/FYP backend algo/Brain tumor frontend/static/uploads1/withskull.gif",
    message: "skullStripped",
    // });
  });
});

app.post("/", upload.single("image"), async (req, res) => {
  //const url = req.query.url;
  var start = new Date().getTime();

  //alert("Execution time: " + time);
  const url = "uploads1/" + req.query.name + req.file.originalname;
  console.log(req.file.originalname);
  var name = req.query.name;
  console.log("URL" + url);
  var dataToSend;
  //var v = "uploads1/00000.mnc";
  // spawn new child process to call the python script C:\Users\DELL\Desktop\FYP backend algo\Brain tumor frontend\static\uploads1\00000.mnc
  const python = await spawn("python", ["strip.py", url, "bilal"]); //uploads1\00000.mnc
  // collect data from script
  python.stdout.on("data", function (data) {
    console.log("Pipe data from python script ...");
    dataToSend = data.toString();
  });
  // in close event we are sure that stream from child process is closed
  await python.on("close", (code) => {
    console.log(`child process close all stdio with code ${code}`);
    // send data to browser
    // res.send(dataToSend);
    var end = new Date().getTime();
    var time = end - start;
    console.log("Total Time taken" + time / 1000);
    if (code === 0) {
      return res.json({
        withoutskull: `img/${name}/withoutskull.gif`,
        withskull: `img/${name}/withskull.gif`,
        message: "skullStripped",
      });
    } else {
      return res.json({
       
        message: "notskullStripped",
      });
    }
  });
});

const PORT = process.env.PORT || 3002;

app.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});
