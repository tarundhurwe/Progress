import React, { useEffect, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import NavBar from './NavBar'
import api from "../api";
import "../assets/css/problemSet.css"

const ProblemList = () => {
    const { problem_set_id } = useParams()
    const [problems, setProblems] = useState([])
    const [marked, setMarked] = useState(false)

    useEffect(() => {
        getProblems();
    }, [])
    const getProblems = () => {
        api
            .get(`/api/problems/${problem_set_id}`)
            .then((res) => res.data)
            .then((data) => setProblems(data)).catch((err) => alert(err));
    }

    const markProblem = (problem_id, pos) => {
        api
            .put(`/api/problems/mark/${problem_id}`)
            .then((res) => res.data)
            .then((data) => { setMarked(true); toggle(pos) }).catch((err) => alert(err));
    }

    function toggle(pos) {
        let ele = document.getElementById(pos)
        let original = window.getComputedStyle(ele, null).getPropertyValue('color')
        if (original === "rgb(0, 128, 0)") {
            document.getElementById(pos).style.color = "#D3D3D3"
        }
        else {
            document.getElementById(pos).style.color = "green"
        }
    }

    return (
        <>
            <NavBar />


            <div className="relative overflow-x-auto shadow-md sm:rounded-lg problem-set">
                <table className="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                        <tr>
                            <th scope="col" className="px-6 py-3">
                                S No.
                            </th>
                            <th scope="col" className="px-6 py-3">
                                Problem name
                            </th>
                            <th scope="col" className="px-6 py-3">
                                Problem type
                            </th>
                            <th scope="col" className="px-6 py-3">
                                Status
                            </th>
                            <th scope="col" className="px-6 py-3">
                                <span className="sr-only">Notes</span>
                            </th>
                        </tr>
                    </thead>
                    <tbody>

                        {problems.map((e, index) => {
                            return (
                                <tr className="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600" key={e.problem_id}>
                                    <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                                        {index + 1}
                                    </th>
                                    <td className="px-6 py-4">
                                        <a href={e.problem_link} target="_blank">{e.problem_name}</a>
                                    </td>
                                    <td className="px-6 py-4">
                                        {e.problem_type}
                                    </td>
                                    <td className="px-6 py-4">
                                        <svg className="w-6 h-6 text-gray-600 dark:text-gray" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" onClick={() => markProblem(e.problem_id, index)}>
                                            {e.status === true ? (<path stroke="currentColor"
                                                id={(index)}
                                                strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M8.5 11.5 11 14l4-4m6 2a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" style={{ color: "green" }} />) :
                                                (<path stroke="currentColor"
                                                    id={(index)} strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M8.5 11.5 11 14l4-4m6 2a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" style={{ color: "#D3D3D3" }} />)}
                                        </svg>
                                    </td>
                                    <td className="px-6 py-4 text-right">
                                        <a href="#" className="font-medium text-blue-600 dark:text-blue-500 hover:underline">Notes</a>
                                    </td>
                                </tr>
                            )
                        })}

                    </tbody>
                </table>
            </div>

        </>
    )
}

export default ProblemList

