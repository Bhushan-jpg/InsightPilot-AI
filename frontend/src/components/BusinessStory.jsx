import "./BusinessStory.css";

function BusinessStory({ data }) {

    if (!data || !data.business_story) {
        return null;
    }

    return (

        <div className="card">

            <h2>📖 Business Story</h2>

            <p className="story-text">

                {data.business_story}

            </p>

        </div>

    );

}

export default BusinessStory;