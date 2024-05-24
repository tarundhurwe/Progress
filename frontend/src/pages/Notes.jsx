import React, { useEffect } from "react";
import ReactQuill from "react-quill";
import "react-quill/dist/quill.snow.css";
import { useState } from "react";
import "../assets/css/notes.css";
import { useParams } from "react-router-dom";
import api from "../api";
import NavBar from "./NavBar";

const Notes = () => {
  const [editorValue, setEditorValue] = useState("");
  const { problem_id } = useParams();
  const [problem, setProblem] = useState({});
  const [title, setTitle] = useState("");

  useEffect(() => {
    getProblem();
  }, []);

  const getProblem = async () => {
    try {
      const response = await api.get(`/api/problems/individual/${problem_id}`);
      if (response !== null) {
        setProblem(response.data);
      }
    } catch (err) {
      console.log(err);
    }
  };

  useEffect(() => {
    getNote();
  }, []);

  const getNote = async () => {
    try {
      const response = await api.get(`/api/problems/note/${problem_id}`);
      if (response !== null) {
        setTitle(response.data["title"]);
        setEditorValue(response.data["content"]);
      }
    } catch (err) {
      console.log(err);
    }
  };

  const handleSave = async () => {
    try {
      const response = await api.post(
        `/api/problems/note/update/${problem_id}`,
        {
          title: title,
          content: editorValue,
        }
      );
      if (response !== null) {
        alert("Note saved successfully");
      }
    } catch (err) {
      console.error("Error saving note: ", err);
    }
  };

  return (
    <>
      <NavBar />
      <div className="relative overflow-x-auto mb-5 desc">
        <table className="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
          <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
              <th scope="col" className="px-6 py-3">
                Problem Category
              </th>
              <th scope="col" className="px-6 py-3">
                Problem
              </th>
            </tr>
          </thead>
          <tbody>
            <tr className="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
              <th
                scope="row"
                className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
              >
                {problem["problem_type"]}
              </th>
              <td className="px-6 py-4">
                <a href={problem["problem_link"]} target="__blank">
                  {problem["problem_name"]}
                </a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <form className="space-y-6 notes-form" onSubmit={handleSave}>
        <div className="mb-6" style={{ width: "80vw", margin: "auto" }}>
          <label
            htmlFor="default-input"
            className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
          >
            Title
          </label>
          <input
            type="text"
            id="default-input"
            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder={problem["problem_name"]}
            required
          />
        </div>
        <ReactQuill
          value={editorValue}
          onChange={(value) => setEditorValue(value)}
        />
        <div className="submit-btn">
          <button
            type="submit"
            className="text-white bg-gradient-to-r from-blue-500 via-blue-600 to-blue-700 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2"
          >
            Save
          </button>
        </div>
      </form>
    </>
  );
};

export default Notes;
