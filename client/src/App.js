import React, { useState, useEffect } from 'react'
import { Switch, useLocation } from 'react-router-dom';

import { AuthContext} from './context';
import { ProtectedRoute, AuthRoute } from './Routes'
import Landing from './components/Landing'
import Home from './components/Home'
import Signup from './components/auth/Signup'

const App = () => {
    const [fetchWithCSRF, setFetchWithCSRF] = useState(() => fetch);
    const [currentUserId, setCurrentUserId] = useState(null);
    const [loading, setLoading] = useState(true);
    const [otherUserId, setOtherUserId] = useState(null);

    const authContextValue = {
        fetchWithCSRF,
        currentUserId,
        setCurrentUserId,
        otherUserId,
        setOtherUserId
    }

    useEffect(() => {
        async function restoreCSRF() {
            const response = await fetch('/api/csrf/restore', {
                method: 'GET',
                credentials: 'include'
            });
            if (response.ok) {
                const authData = await response.json();
                setFetchWithCSRF(() => {
                    return (resource, init) => {
                        if (init.headers) {
                            init.headers['X-CSRFToken'] = authData.csrf_token;
                        } else {
                            init.headers = {
                                'X-CSRFToken': authData.csrf_token,
                            };
                        }
                        return fetch(resource, init);
                    };
                });
                if (authData.current_user_id) {
                    setCurrentUserId(authData.current_user_id);
                }
            }
            setLoading(false);
        }
        restoreCSRF();
    }, []);

    if (loading) {
        return null;
    }

    return (
        <AuthContext.Provider value={authContextValue}>
                <Switch >
                    <AuthRoute path='/landing' component={Landing} />
                    <AuthRoute
                        path="/Signup"
                        component={Signup}
                        currentUserId={currentUserId}
                    />
                    <ProtectedRoute
                        path="/"
                        exact
                        component={Home}
                        currentUserId={currentUserId}
                    />

                </Switch>
        </AuthContext.Provider>
    )
}


export default App;
