import React from "react";
import { useState, useEffect } from "react";
import api from "../api";
import ProblemSetList from "./ProblemSetList";
import FailureBanner from "./FailureBanner";
import NavBar from "./NavBar";

const Home = () => {
  const [problemsList, setProblemList] = useState([]);

  useEffect(() => {
    getProblemList();
  }, []);

  const getProblemList = () => {
    api
      .get("/api/")
      .then((res) => res.data)
      .then((data) => {
        setProblemList(data);
      })
      .catch((err) => alert(err));
  };

  return (
    <>
      <NavBar />
      <ProblemSetList problemset={problemsList} />
    </>
  );
};

export default Home;
