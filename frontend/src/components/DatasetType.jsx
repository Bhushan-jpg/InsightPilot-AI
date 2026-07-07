import "./DatasetType.css";

function DatasetType({ data }) {

    if (!data || !data.dataset_type) return null;

    return (

        <div className="dataset-type-card">

            <h2>🎯 Dataset Type</h2>

            <h1>
                {data.dataset_type.icon} {data.dataset_type.type}
            </h1>

            <p>
                AI Confidence : {data.dataset_type.confidence}%
            </p>

        </div>

    );

}

export default DatasetType;