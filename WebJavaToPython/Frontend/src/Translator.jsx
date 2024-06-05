import { useState, useEffect } from "react";
import { TranslatorWindow } from "./components";

function Translator() {
  const JavaColor =
    "from-red-600 from-10% via-blue-700 via-30% via-blue-700 to-violet-600 to-95%";
  const PythonColor =
    "from-yellow-400 from-5% via-emerald-700 via-35% to-green-300";

  const [javaCode, setJavaCode] = useState("");
  const [pythonCode, setPythonCode] = useState("");
  const [file, setFile] = useState("");
  const [error, setError] = useState("");

  useEffect(() => {
    if (javaCode) {
      // Ensure there's something to translate
      translateCode();
    }
  }, [javaCode]); // Only run when javaCode changes

  const handleJavaInputChange = (event) => {
    setJavaCode(event.target.value);
  };

  const translateCode = async () => {
    try {
      const response = await fetch("http://localhost:5000/translate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ javaCode }),
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const data = await response.json();
      setPythonCode(data.pythonCode);
    } catch (error) {
      setError("Failed to translate code");
      console.error("Error:", error);
    }
  };

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        const text = e.target.result;
        setJavaCode(text); // setState and rely on useEffect to trigger translation
      };
      reader.readAsText(file);
    }
  };

  // Dummy translation function (replace with actual API call)

  const downloadFile = (data, filename, type = "text/plain") => {
    const file = new Blob([data], { type: type });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(file);
    a.download = filename;
    a.click();
  };

  const handleDownloadPython = () => {
    downloadFile(pythonCode, `${file}.py`, "text/plain");
  };

  return (
    <div>
      <div className="flex flex-row justify-center gap-20 px-20 h-[60vh] ">
        <TranslatorWindow
          name="Java"
          code={javaCode}
          handler={handleJavaInputChange}
          color={JavaColor}
        />
        <TranslatorWindow
          name="Python"
          code={pythonCode}
          readOnly
          color={PythonColor}
        />
      </div>
      <div className="flex flex-row justify-around items-center pt-16">
        {/* <input
          type="file"
          onChange={handleFileUpload}
          className="cursor-pointer bg-slate-800 text-color-200 font-bold "
        /> */}
        <div className="flex flex-col">
          <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
            Upload file
          </label>
          <input
            onChange={handleFileUpload}
            className="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-600"
            type="file"
          />
        </div>

        <button
          onClick={handleDownloadPython}
          className="bg-gradient-to-br from-blue-600 to-blue-400 text-white font-bold py-2 px-4 rounded-lg"
        >
          Download
        </button>
      </div>
    </div>
  );
}

export default Translator;
