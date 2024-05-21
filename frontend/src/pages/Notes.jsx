import React from "react";
import ReactQuill from "react-quill";
import "react-quill/dist/quill.snow.css";
import { useState } from "react";
import "../assets/css/notes.css";

const Notes = () => {
  const [editorValue, setEditorValue] = useState("");

  return (
    <>
      <ReactQuill
        value={editorValue}
        onChange={(value) => setEditorValue(value)}
      />
    </>
  );
};

export default Notes;
