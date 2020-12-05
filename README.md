   ```bash
   pipenv install --dev -r dev-requirements.txt --python=python3 && pipenv install -r requirements.txt
   ```

```bash
   python -m database && flask run
```

```python
import React, { useState} from 'react';
import { useHistory, NavLink } from 'react-router-dom';



const Component = () => {

    const handleChange = e => {
        setInput(e.target.value)
    }

    const handleSubmit = () => {
        history.push('/search')
    }

    return (
        <div className='component'>
        </div>
    )
}

export default Component;
```
