export function DisplayArea({ type, data }) {
    if (type == 'summary') {
        return <ul>
            <li>Total Organizations: {data.totalOrgs}</li>
            <li>Total Owners: {data.totalOwners}</li>
            <li>Total Repos: {data.totalRepos}</li>
            <li>Total Issues: {data.totalIssues}</li>
        </ul>
    } else if (type == 'rank_all') {
        
        return <table>
            <tr>
                <th>Repository</th>
                <th>Owner</th>
                <th># Issues</th>
                <th>Ranking</th>
            </tr>
            {data.rankings.map((repoData) => <tr key={repoData[0]}>
                <th>{repoData[0]}</th>
                <th>{repoData[1]}</th>
                <th>{repoData[2]}</th>
                <th>{repoData[3]}</th>
            </tr>)}
        </table>
    } else {
        return <></>
    }
}