import React from 'react'
import "../assets/css/problemSet.css"
import { Link } from 'react-router-dom'

const ProblemSetList = ({ problemset }) => {
    return (
        <>

            <div className="relative overflow-x-auto problem-set">
                <table className="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                        <tr>
                            <th scope="col" className="px-6 py-3">
                                S No.
                            </th>
                            <th scope="col" className="px-6 py-3">
                                Problem set
                            </th>
                            <th scope="col" className="px-6 py-3">
                                Author
                            </th>
                            <th scope="col" className="px-6 py-3">
                                Link
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        {problemset.map((e) => {
                            return (<tr className="bg-white border-b dark:bg-gray-800 dark:border-gray-700" key={e.problem_set_id}>
                                <td scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                                    {e.problem_set_id + 1}
                                </td>
                                <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                                    <Link to={`/problems/${e.problem_set_id}`}>{e.problem_set_name}</Link>
                                </th>
                                <td className="px-6 py-4">
                                    {e.author}
                                </td>
                                <td className="px-6 py-4">
                                    <a href={e.link} target='__blank'>{e.link}</a>
                                </td>
                            </tr>)
                        })}
                    </tbody>
                </table>
            </div>

        </>
    )
}

export default ProblemSetList